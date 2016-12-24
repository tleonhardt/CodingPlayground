import hello

def test_valid(capsys):
    name = "Todd"
    hello.say_hello_to(name)
    out, _ = capsys.readouterr()
    assert out == "Hello {}!\n".format(name)
