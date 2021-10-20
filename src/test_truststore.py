import pytest
from OpenSSL.crypto import FILETYPE_ASN1, FILETYPE_PEM, Error
from tlstrust import TrustStore

pem = """
-----BEGIN CERTIFICATE-----
MIIBtjCCAVugAwIBAgITBmyf1XSXNmY/Owua2eiedgPySjAKBggqhkjOPQQDAjA5
MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6b24g
Um9vdCBDQSAzMB4XDTE1MDUyNjAwMDAwMFoXDTQwMDUyNjAwMDAwMFowOTELMAkG
A1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJvb3Qg
Q0EgMzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABCmXp8ZBf8ANm+gBG1bG8lKl
ui2yEujSLtf6ycXYqm0fc4E7O5hrOXwzpcVOho6AF2hiRVd9RFgdszflZwjrZt6j
QjBAMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMB0GA1UdDgQWBBSr
ttvXBp43rDCGB5Fwx5zEGbF4wDAKBggqhkjOPQQDAgNJADBGAiEA4IWSoxe3jfkr
BqWTrBqYaGFy+uGh0PsceGCmQ5nFuMQCIQCcAu/xlJyzlvnrxir4tiz+OpAUFteM
YyRIHN8wfdVoOw==
-----END CERTIFICATE-----"""
der = b'0\x82\x01\xb60\x82\x01[\xa0\x03\x02\x01\x02\x02\x13\x06l\x9f\xd5t\x976f?;\x0b\x9a\xd9\xe8\x9ev\x03\xf2J0\n\x06\x08*\x86H\xce=\x04\x03\x02091\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x0f0\r\x06\x03U\x04\n\x13\x06Amazon1\x190\x17\x06\x03U\x04\x03\x13\x10Amazon Root CA 30\x1e\x17\r150526000000Z\x17\r400526000000Z091\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x0f0\r\x06\x03U\x04\n\x13\x06Amazon1\x190\x17\x06\x03U\x04\x03\x13\x10Amazon Root CA 30Y0\x13\x06\x07*\x86H\xce=\x02\x01\x06\x08*\x86H\xce=\x03\x01\x07\x03B\x00\x04)\x97\xa7\xc6A\x7f\xc0\r\x9b\xe8\x01\x1bV\xc6\xf2R\xa5\xba-\xb2\x12\xe8\xd2.\xd7\xfa\xc9\xc5\xd8\xaam\x1fs\x81;;\x98k9|3\xa5\xc5N\x86\x8e\x80\x17hbEW}DX\x1d\xb37\xe5g\x08\xebf\xde\xa3B0@0\x0f\x06\x03U\x1d\x13\x01\x01\xff\x04\x050\x03\x01\x01\xff0\x0e\x06\x03U\x1d\x0f\x01\x01\xff\x04\x04\x03\x02\x01\x860\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\xab\xb6\xdb\xd7\x06\x9e7\xac0\x86\x07\x91p\xc7\x9c\xc4\x19\xb1x\xc00\n\x06\x08*\x86H\xce=\x04\x03\x02\x03I\x000F\x02!\x00\xe0\x85\x92\xa3\x17\xb7\x8d\xf9+\x06\xa5\x93\xac\x1a\x98har\xfa\xe1\xa1\xd0\xfb\x1cx`\xa6C\x99\xc5\xb8\xc4\x02!\x00\x9c\x02\xef\xf1\x94\x9c\xb3\x96\xf9\xeb\xc6*\xf8\xb6,\xfe:\x90\x14\x16\xd7\x8cc$H\x1c\xdf0}\xd5h;'

def test_properties():
    ts = TrustStore(FILETYPE_ASN1, der)
    assert isinstance(ts, TrustStore)
    assert isinstance(ts.fingerprint_sha256, str)
    assert isinstance(ts.fingerprint_sha1, str)

def test_no_args():
    with pytest.raises(TypeError):
        TrustStore()

def test_no_format_arg():
    with pytest.raises(AttributeError):
        TrustStore('', None)

def test_no_cacert_arg():
    with pytest.raises(Error):
        TrustStore(FILETYPE_PEM, None)

def test_pem_format():
    ts = TrustStore(FILETYPE_PEM, pem)
    assert isinstance(ts.is_trusted(), bool)

def test_is_trusted_context_type():
    ts = TrustStore(FILETYPE_PEM, pem)
    with pytest.raises(TypeError):
        ts.is_trusted('apple')

def test_is_trusted_bad_context():
    ts = TrustStore(FILETYPE_PEM, pem)
    with pytest.raises(AttributeError):
        ts.is_trusted(99999)

def test_result():
    ts = TrustStore(FILETYPE_PEM, pem)
    assert ts.trusted_by_android()
    assert ts.trusted_by_apple()
    assert ts.trusted_by_ccadb()
    assert ts.trusted_by_java()
    assert ts.trusted_by_linux()
    assert ts.trusted_by_certifi()
