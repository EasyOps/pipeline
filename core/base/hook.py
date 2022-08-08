

class Hook:

    def on_fit_start(self):
        raise NotImplementedError()

    def on_fit_end(self):
        raise NotImplementedError()

    def on_train_start(self):
        raise NotImplementedError()

    def on_train_end(self):
        raise NotImplementedError()

    def on_validation_start(self):
        raise NotImplementedError()

    def on_validation_end(self):
        raise NotImplementedError()

    def on_test_start(self):
        raise NotImplementedError()

    def on_test_end(self):
        raise NotImplementedError()

    def on_predict_start(self):
        raise NotImplementedError()

    def on_predict_end(self):
        raise NotImplementedError()

    