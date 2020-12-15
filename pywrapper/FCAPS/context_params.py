from FCAPS.shared_utils import ModuleSetting

class ContextBasedComputationProcedure(ModuleSetting):
    def __init__(self, context_file_path: str, processor: ModuleSetting):
        super().__init__('ComputationProcedureModules', 'ContextBasedComputationProcedureModule')
        self.params = {
            "ContextFilePath": context_file_path,
            "ContextProcessor": processor.to_dict()
        }

class AddIntentContextProcessor(ModuleSetting):
    def __init__(self, pattern_manager: ModuleSetting, min_extent_size: int = 1, min_lift: int = 1, min_stab: int = 1, out_extent: bool = True, out_support: bool = False, out_order: bool = True, out_stab_estimation: bool = True, out_stability: bool = True, is_log_stability: bool = True):
        super().__init__('ContextProcessorModules', 'AddIntentContextProcessorModule')
        if min_extent_size < 1:
            raise ValueError('min_extent_size should be greater or equal 1')
        if min_lift < 1:
            raise ValueError('min_lift should be greater or equal 1')
        self.params = {
            "PatternManager": pattern_manager.to_dict(),
            "OutputParams": {
                # The minimal size of concept extent for reporting the concept
                "MinExtentSize": min_extent_size,
                # The minimum DELTA-measure for reported concept
                "MinLift": min_lift,
                # The minimum stability of a concept to be reported
                "MinStab": min_stab,
                # A flag indicating if the extent should be reported
                "OutExtent": out_extent,
                # A flag indicating if the support of concept should be reported
                "OutSupport": out_support,
                # A flag indicating if the order of filtered concepts should be found and reported"A flag indicating if the order of filtered concepts should be found and reported
                "OutOrder": out_order,
                # A flag indicating if stability estimate should be reported
                "OutStabEstimation": out_stab_estimation,
                # A flag indicating if the stability should be computed and reported
                "OutStability": out_stability,
                # A flag indicating if stability should be reported in log scale (more readable for stability close to one)
                "IsStabilityInLog": is_log_stability
            }
        }

class BinarySetJoinPatternManager(ModuleSetting):
    def __init__(self, use_names: bool = True, use_inds: bool = False):
        super().__init__('PatternManagerModules', 'BinarySetJoinPatternManagerModule')
        self.params = {
            # Should write pattern attributes by their names
            "UseNames": use_names,
            # Should write pattern attributes by their indices
            "UseInds": use_inds
        }


class BinarySetUnionPatternManager(ModuleSetting):
    def __init__(self, use_names: bool = True, use_inds: bool = False):
        super().__init__('PatternManagerModules', 'BinarySetUnionPatternManagerModule')
        self.params = {
            # Should write pattern attributes by their names
            "UseNames": use_names,
            # Should write pattern attributes by their indices
            "UseInds": use_inds
        }