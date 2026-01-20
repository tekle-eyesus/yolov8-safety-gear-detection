"""Entry point for the safety gear detection app."""

from app.utils.inference import load_model
from app.utils.ui import run_ui


def main() -> None:
    """Launch the UI after loading the model."""
    model = load_model()
    run_ui(model)


if __name__ == "__main__":
    main()
