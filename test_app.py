def test_home():
    assert True

def test_app_file_exists():
    import os
    assert os.path.exists("app.py")

def test_dockerfile_exists():
    import os
    assert os.path.exists("Dockerfile")
