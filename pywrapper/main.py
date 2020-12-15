from FCAPS.context_params import ContextBasedComputationProcedure, AddIntentContextProcessor, BinarySetJoinPatternManager
from FCAPS.subgroup_discovery import BestPatternFirstComputationProcedure, StabilityCbOLocalProjectionChain, SAXJsonContextAttributes, BinaryClassificationOptimisticEstimator

from FCAPS.context import Context
from FCAPS.runner import Runner

context = Context(
    obj_names=[
        "fish leech",
        "bream",
        "frog",
        "dog",
        "water weeds",
        "reed",
        "bean",
        "corn"
    ],
    attr_names=[
        "needs water to live",
        "lives in water",
        "lives on land",
        "needs chlorophyll",
        "dicotyledon",
        "monocotyledon",
        "can move",
        "has limbs",
        "breast feeds"
    ],
    connections=[
        [0,1,6],
        [0,1,6,7],
        [0,1,2,6,7],
        [0,2,5,7,8],
        [0,1,3,5],
        [0,1,2,3,5],
        [0,2,3,4],
        [0,2,3,5]
    ]
)
MY_CONTEXT_FILENAME = 'mycontext.json' 
context.to_file(MY_CONTEXT_FILENAME)
context_processor = ContextBasedComputationProcedure(
    context_file_path=MY_CONTEXT_FILENAME,
    processor = AddIntentContextProcessor(
        pattern_manager=BinarySetJoinPatternManager(
            use_names=True,
            use_inds=False
        ),
        min_extent_size=2,
        min_lift=1,
        min_stab=1,
        out_extent=True,
        out_support=False,
        out_order=True,
        out_stability=True,
        out_stab_estimation=True,
        is_log_stability=True
    )
)

processor = BestPatternFirstComputationProcedure(
    max_ram_consumption = 2000000000,
    max_pattern_number = 30000,
    default_threshold = 3,
    adjust_threshold = False,
    local_projection_chain = StabilityCbOLocalProjectionChain(
        all_attributes_in_once = True,
        context_attributes = SAXJsonContextAttributes(
            context_file_path = 'titanic.json'
        )
    ),
    optimistic_estimator = BinaryClassificationOptimisticEstimator(
        target_classes = ["1"], 
        classes_path = 'survived.json',
        freq_weight = 0.1
    )
)
result = Runner().setCustomContextProcessor(processor).run()
print(result[0][1]["Nodes"])
