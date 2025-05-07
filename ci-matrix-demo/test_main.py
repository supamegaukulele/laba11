from main import is_prime

def test_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(13)
    assert is_prime(97)

def test_non_primes():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(100)
