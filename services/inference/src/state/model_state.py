from sklearn.pipeline import Pipeline


class ModelState:
    def __init__(self):
        self.model_id: str | None = None
        self.model: Pipeline | None = None


model_state = ModelState()