from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
import re

code_base_model = apps.get_model('users', 'CodeBase')


def all_scan_filter(rfid_code):
    """
    Function to clean the RFID Code
    """
    rfid_code = re.sub(r'[\x00-\x1F]+', '', rfid_code)
    return rfid_code


def check_owner(rfid_code):
    """
    Function to check and return the owner of
    an RFID Code or return None if there's no owner
    """
    rfid_code = all_scan_filter(rfid_code)
    try:
        code_base_obj = code_base_model.objects.get(rfid_code=rfid_code)
        return code_base_obj.owner
    except ObjectDoesNotExist:
        return None


def update_rfid_code(instance=None, new_rfid_code=None):

    #  check if an owner exists for the rfid code supplied
    rfid_code = all_scan_filter(new_rfid_code)
    owner = check_owner(rfid_code=rfid_code)

    if not owner:  # Doesn't belong to anybody
        if instance.rfid_code.all():
            # Update
            inst = instance.rfid_code.all()[0]
            inst.rfid_code = rfid_code
            inst.save()
        else:
            # Create
            new_codebase = code_base_model(owner=instance, rfid_code=rfid_code)
            new_codebase.save()
        return {"success": True, "owner": instance.rfid_code.all()[0]}
    else:  # RFID code belongs to an owner
        return {"success": False, "owner": owner}
