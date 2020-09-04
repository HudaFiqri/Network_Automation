import paramiko
import os


def test(value1, value2):
    return int(value1) + int(value2)

a = test('2', '4')

print(a)