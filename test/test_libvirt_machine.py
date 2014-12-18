import unittest
import utils
import lxml.etree


class LibvirtMachineBase64UserdataTestCase(unittest.TestCase):
    def setUp(self):
        self.machine = utils.machine_resolver.LibvirtMachine('192.168.0.1', lxml.etree.parse(open(
                                                                            'test/static/base64_userdata_domain.xml')))

    def test_userdata(self):
        self.assertEqual(self.machine.get_userdata(),
                         "#cloud-config\ndisable_root: False\nssh_pwauth: False\nmanage_etc_hosts: False\n"
                         "multiple:\n  indentation:\n    levels: are cool")


class LibvirtMachineTestCase(unittest.TestCase):
    def setUp(self):
        self.machine = utils.machine_resolver.LibvirtMachine('192.168.0.1',
                                                             lxml.etree.parse(open('test/static/metadata_domain.xml')))

    def test_instance_id(self):
        self.assertEqual(self.machine.get_instance_id(), 'i-12345678')

    def test_public_ipv4(self):
        self.assertEqual(self.machine.get_public_ipv4(), '192.168.0.1')

    def test_local_ipv4(self):
        self.assertEqual(self.machine.get_local_ipv4(), '192.168.0.1')

    def test_placement_availability_zone(self):
        self.assertEqual(self.machine.get_placement_availability_zone(), 'us-east-1a')

    def test_userdata(self):
        self.assertEqual(self.machine.get_userdata(),
                         "#cloud-config\ndisable_root: False\nssh_pwauth: False\nmanage_etc_hosts: False\n"
                         "multiple:\n  indentation:\n    levels: are cool")

    def test_keys(self):
        keys = self.machine.get_keys()

        # make sure the keys are ordered properly
        self.assertEquals(keys.keys()[0], 'my-public-key2')
        self.assertEquals(keys.keys()[1], 'my-public-key1')

        self.assertDictEqual(keys['my-public-key1'], {'openssh-key': 'ssh-rsa my-public-key1 foo@bar'})
        self.assertDictEqual(keys['my-public-key2'], {'openssh-key': 'ssh-rsa my-public-key2 foo@bar',
                                                      'another-format': 'a different format'})
