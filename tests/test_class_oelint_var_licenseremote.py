import pytest
from base import TestBaseClass


class TestClassOelintVarLicenseRemoteFile(TestBaseClass):

    @pytest.mark.parametrize('id', ['oelint.var.licenseremotefile'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input', 
        [
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://${COMMON_LIC_DIR}/MIT;md5=sjdjasdjhddh"
            '''
            },
            {
            'oelint_adv_test.bb':
            '''
            A = "${COMMON_LIC_DIR}"
            LIC_FILES_CHKSUM = "file://${A}/MIT;md5=sjdjasdjhddh"
            '''
            }
        ],
    )
    def test_bad(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)

    @pytest.mark.parametrize('id', ['oelint.var.licenseremotefile'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input', 
        [
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://LICENSE;md5=sjdjasdjhddh"
            '''
            },
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://${WORKDIR}/LICENSE;md5=sjdjasdjhddh"
            '''
            },
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://${S}/LICENSE;md5=sjdjasdjhddh"
            '''
            },
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://${B}/LICENSE;md5=sjdjasdjhddh"
            '''
            },
            {
            'oelint_adv_test.bb':
            '''
            LIC_FILES_CHKSUM = "file://${A}/LICENSE;md5=sjdjasdjhddh"
            A = "${WORKDIR}"
            '''
            },
        ],
    )
    def test_good(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)
