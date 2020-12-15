from FCAPS.shared_utils import ModuleSetting
from typing import List

class StabilityCbOLocalProjectionChain(ModuleSetting):
    def __init__(self, context_attributes: ModuleSetting, all_attributes_in_once: bool = True, reserve_memory: int = 256):
        super().__init__('LocalProjectionChainModules', 'StabilityCbOLocalProjectionChainModule')
        if reserve_memory <= 0:
            raise ValueError('reserve_memory should be positive')
        self.params = {
            # When called to compute next projection should it be generated only one 'next' pattern with one attribute, or all of them
            "AllAttributesInOnce": all_attributes_in_once,
            # A module for storing and accesing formal context
            "ContextAttributes": context_attributes.to_dict(),
            # A number of patterns to be reserved
            "ReserveMemory": reserve_memory,
        }


class BestPatternFirstComputationProcedure(ModuleSetting):
    def __init__(self, local_projection_chain: ModuleSetting, optimistic_estimator: ModuleSetting, max_ram_consumption: int = 2000000000, max_pattern_number: int = 30000, default_threshold: int = 3, adjust_threshold: bool = False, optimistic_estimator_min_quality: float = -1e10, break_on_first_subgroup: bool = False, compute_for_all_thresholds: bool = False, beams_number: int = 1):
        super().__init__('ComputationProcedureModules', 'BestPatternFirstComputationProcedureModule')
        if max_pattern_number <= 0:
            raise ValueError('max_pattern_number should be positive')
        if max_ram_consumption <= 0:
            raise ValueError('max_ram_consumption should be positive')
        if beams_number <= 0:
            raise ValueError('beams_number should be positive')
        self.params = {
            # The maximal amount of RAM to be used to store the patterns. The number is approximate.
            "MaxRAMConsumption": max_ram_consumption,
            # The maximal number of patterns that should be stored at any iteration of the algorithm. Used only when 'AdjustThreshold' is true.
            "MaxPatternNumber": max_pattern_number,
            # The initial threshold for DELTA-measure (or any other projection-antimonotonic measure).
            "DefualtThld": default_threshold,
            # A flag indicating if the threshold should be adjusted in order to ensure polynomiality and memory finity
            "AdjustThreshold": adjust_threshold,
            # The projection chain that allows for finding preimages for any pattern with its special projection chain.
            "LocalProjectionChain": local_projection_chain.to_dict(),
            # The object that defines the optimistic estimator for the goal function
            "OptimisticEstimator": optimistic_estimator.to_dict(),
            # The minimal quality of the pattern that is considederd interesting to be found
            "OEstMinQuality": optimistic_estimator_min_quality,
            # Stop the computation when the first subgroup with sufficient quality is found
            "BreakOnFirstSD": break_on_first_subgroup,
            # If false, then the computation stops when it understand that for the current threshold the best pattern is known. Otherwise it computes for all thlds, starting from the first one.
            "ComputeForAllThlds": compute_for_all_thresholds,
            # The number of beams to be used for expansion of a concept from the queue
            "BeamsNumber": beams_number
        }


class SAXJsonContextAttributes(ModuleSetting):
    def __init__(self, context_file_path: str):
        super().__init__('ContextAttributesModules', 'SAXJsonContextAttributesModule')
        self.params = {
            # Path to context file
            "ContextFilePath": context_file_path
        }


class BinaryClassificationOptimisticEstimator(ModuleSetting):
    def __init__(self, target_classes: List[str], classes_path: str, freq_weight: float = 0.1):
        super().__init__('OptimisticEstimatorModules', 'BinaryClassificationOptimisticEstimatorModule')
        if freq_weight > 1.0 or freq_weight < 0.0:
            raise ValueError('freq_weight should be between 0.0 and 1.0')
        self.params = {
            # Array fo strings that gives the classes that would be all together considered as a traget class
            "TargetClasses": target_classes,
            # The path to a file, containing the class labels for every object
            "Classes": classes_path,
            # A weight for the frequence part in the resulting formula  should be less than 1. If 1 frequency part is considered with the same weight to probability part.
            "FreqWeight": freq_weight
        }


class FisherBinClassificationOptimisticEstimator(ModuleSetting):
    def __init__(self, target_classes: List[str], classes_path: str, freq_weight: float = 0.1):
        super().__init__('OptimisticEstimatorModules', 'FisherBinClassificationOptimisticEstimator')
        if freq_weight > 1.0 or freq_weight < 0.0:
            raise ValueError('freq_weight should be between 0.0 and 1.0')
        self.params = {
            # Array fo strings that gives the classes that would be all together considered as a traget class
            "TargetClasses": target_classes,
            # The path to a file, containing the class labels for every object
            "Classes": classes_path,
            # A weight for the frequence part in the resulting formula  should be less than 1. If 1 frequency part is considered with the same weight to probability part.
            "FreqWeight": freq_weight
        }