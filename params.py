
# Project paths:
USER_MODEL_STATE_PATH = "./database/gaze_event_rules.db"
GAZE_EVENT_RULES_PATH = "./database/user_model_state.db"
FRONT_END_STATIC_PATH = "./application/frontend/static/"
FRONT_END_TEMPLATE_PATH = "./application/frontend/template/"

# Platform configuration:
USE_FIXATION_ALGORITHM = True
USE_EMDAT = True
USE_ML = False

# Features to use
USE_PUPIL_FEATURES = True
USE_DISTANCE_FEATURES = True
USE_FIXATION_PATH_FEATURES = True
USE_TRANSITION_AOI_FEATURES = True

# Sets of features to keep
KEEP_TASK_FEATURES = True
KEEP_GLOBAL_FEATURES = True

#Frequency of ML/EMDAT calls:
EMDAT_CALL_PERIOD = 10000
ML_CALL_PERIOD = 6000000

# Some parameter from EMDAT, ask later
MAX_SEG_TIMEGAP= 10

FIX_MAXDIST = 35
FIX_MINDUR = 100000

REST_PUPIL_SIZE = 0
PUPIL_ADJUSTMENT = "rpscenter"
