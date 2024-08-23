from toga_app.boxes import BaseBox


class Factory:

    def __init__(self, box_classes: dict[str, BaseBox]) -> None:
        self.box_classes = box_classes
        for class_name, box_class in self.box_classes.items():
            self.create_box(class_name, box_class)

    def create_box(self, class_name, box_class) -> None:

