import numpy as np
import os
import Stele as hsg
from .fan_compiler import FanCompiler


class FanCompilerWithoutStokes(object):
    """
    Helper class for compiling the data of a polarimetry NIR alpha sweep

    Note: I'm not sure why you would want to use this class anymore. It should
    be deprecated and the standard FanCompiler should be sufficient for all
    needs (and better maintained)

    Typical use scenario:

    datasets = [ ... list of folders, each being a dataset of different NIR
    alphas ...] outputs = FanComilier(<whatever sideband orders you want
    compiled>)
    for data in datasets:
        laserParams, rawData = hsg.hsg_combine_qwp_sweep(folder, save=False,
        verbose=False)_, fitDict = hsg.proc_n_fit_qwp_data(rawData,
        laserParams, vertAnaDir="VAna" in folder, series=folder)
        outputs.addSet(nira, fitDict)
    outputs.buildAndSave(fname)

    """
    def __init__(self, wantedSBs, keepErrors=False, negateNIR=True):
        """

        :param wantedSBs:
        :param keepErrors:
        :param negateNIR: flag for whether to negate the NIR alpha value.
            Currently, this is done because the PAX views -z direction, while
            home-built views +z (with NIR)
        """
        self.want = np.array(wantedSBs)
        # so I can stack in the opposite direction
        self.arrA = wantedSBs.reshape(-1, 1)
        # so I can stack in the opposite direction
        self.arrG = wantedSBs.reshape(-1, 1)
        # so I can stack in the opposite direction
        self.arrS = wantedSBs.reshape(-1, 1)
        self.nirAlphas = []
        self.nirGammas = []
        self._e = keepErrors
        self._n = 1
        if negateNIR:
            print("WARNING: NEGATING NIR ALPHA")
            self._n = -1

    @staticmethod
    def fromDataFolder(
            folder, wantedSBs, keepErrors=False, negateNIR=True):
        """
        Create a fan compiler by passing the data path. Handles looping through
            the folder's sub-folders to find
        :param folder: The folder to search through. Alternatively, if it's a
        list/iterable, iterate through that instead. Useful if external code is
        directly removing sets of data.
        :return:
        """
        comp = FanCompiler(wantedSBs, keepErrors, negateNIR)
        # If it's a string, assume a single path that wants to be searached
        if isinstance(folder, str):
            wantFolders = hsg.natural_glob(folder, "*")
        else:
            # Otherwise, assume they've passed an iterable to search through
            wantFolders = folder

        for nirFolder in wantFolders:
            if "skip" in nirFolder.lower():
                continue
            laserParams, rawData = hsg.hsg_combine_qwp_sweep(
                nirFolder, save=False, verbose=False, loadNorm=False)

            _, fitDict = hsg.proc_n_fit_qwp_data(
                rawData, laserParams, vertAnaDir="VAna" in nirFolder,
                series=nirFolder)
            comp.addSet(fitDict)
        return comp

    def addSet(self, dataSet):
        """ Assume it's passed from  proc_n_fit_qwp_data"""
        newAData = []
        newGData = []
        newSData = []
        alphaSet = dataSet["alpha"]
        gammaSet = dataSet["gamma"]
        s0Set = dataSet["S0"]

        # nirAlpha = dataSet["alpha"][0][1]
        # nirGamma = dataSet["gamma"][0][1]
        if self._e:
            # Need to double to account for
            nirAlpha = [self._n*dataSet["alpha"][0][1], dataSet["alpha"][0][2]]
            nirGamma = [dataSet["gamma"][0][1], dataSet["gamma"][0][2]]
            for sb in self.want:
                # the list(*[]) bullshit is to make sure a list gets appended,
                # not a numpy array. Further complicated because if the list
                # comprehension returns nothing, it doesn't append anything,
                # hence casting to a list.
                newAData.append(
                    list(*[ii[1:] for ii in alphaSet if ii[0] == sb]))
                newGData.append(
                    list(*[ii[1:] for ii in gammaSet if ii[0] == sb]))
                newSData.append(
                    list(*[ii[1:] for ii in s0Set if ii[0] == sb]))
                # no data was found.
                if not newAData[-1]:
                    newAData[-1] = [np.nan, np.nan]
                    newGData[-1] = [np.nan, np.nan]
                    newSData[-1] = [np.nan, np.nan]
        else:
            nirAlpha = [self._n*dataSet["alpha"][0][1]]
            nirGamma = [dataSet["gamma"][0][1]]
            for sb in self.want:
                newAData.append([ii[1] for ii in alphaSet if ii[0] == sb])
                newGData.append([ii[1] for ii in gammaSet if ii[0] == sb])
                newSData.append([ii[1] for ii in s0Set if ii[0] == sb])
                # no data was found.
                if not newAData[-1]:
                    newAData[-1] = [np.nan]
                    newGData[-1] = [np.nan]
                    newSData[-1] = [np.nan]

        try:
            self.arrA = np.column_stack((self.arrA, newAData))
            self.arrG = np.column_stack((self.arrG, newGData))
            self.arrS = np.column_stack((self.arrS, newSData))
        except Exception:
            print(self.arrA.shape)
            print(np.array(newAData).shape)
            raise

        # extending created lists accounts for keeping errors r not
        self.nirAlphas.extend(nirAlpha)
        self.nirGammas.extend(nirGamma)

    def build(self):
        fullDataA = np.append([-1], self.nirAlphas)
        fullDataA = np.row_stack((fullDataA, self.arrA))

        fullDataG = np.append([-1], self.nirGammas)
        fullDataG = np.row_stack((fullDataG, self.arrG))

        fullDataS = np.append([-1], self.nirAlphas)
        fullDataS = np.row_stack((fullDataS, self.arrS))

        return fullDataA, fullDataG, fullDataS

    def buildAndSave(self, fname, *args):
        """
        fname: filename to save to. Must have a least one string formatter
        position to allow for saving separate alpha/gamma/s0 files. *args are
        passed to any other formatting positions.
        :param fname:
        :param args:
        :return:
        """

        if not os.path.exists(os.path.dirname(fname)):
            os.mkdir(os.path.dirname(fname))

        oh = "#\n" * 100
        oh += "\n\n"

        fullDataA, fullDataG, fullDataS = self.build()

        np.savetxt(
            fname.format("alpha", *args), fullDataA, header=oh, delimiter=',',
            comments=''
            )

        np.savetxt(
            fname.format("gamma", *args), fullDataG, header=oh, delimiter=',',
            comments=''
            )

        np.savetxt(
            fname.format("S0", *args), fullDataS, header=oh, delimiter=',',
            comments=''
            )
