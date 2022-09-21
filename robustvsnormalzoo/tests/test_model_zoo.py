import robustvsnormalzoo
import robustvsnormalzoo.utils as utils


def test_own_models():
    model = robustvsnormalzoo.load_model("cifar10", "Huang2020Self", False)
    assert model is not None


def test_rb_models():
    model = robustvsnormalzoo.load_model("cifar10", "Huang2020Self", True)
    assert model is not None


def test_timm_models():
    model = robustvsnormalzoo.load_model("imagenet", "Salman2020Do_R18", False)
    assert model is not None


def test_completeness():
    robustvsnormalzoo.download_all_checkpoints()
    assert True
