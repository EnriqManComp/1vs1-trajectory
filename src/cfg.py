from types import SimpleNamespace

#

cfg = SimpleNamespace(**{})
# Counter model
cfg.n_model = "no_movement_evasor"

# Model save path
cfg.base_save_path =  f"./models/{cfg.n_model}/"
cfg.model_save_path = f"./models/{cfg.n_model}/model.h5"
# Actions
cfg.ACTIONS = {
        0: "NO ACTION",            
        1: "UP",
        2: "DOWN",
        3: "LEFT",
        4: "RIGHT"                    
    }

cfg.EPISODES = 10_000
cfg.COLLECT_DATA = 5_000
cfg.TEST = 20

cfg.GAMMA = 0.99

cfg.TIME = 1600