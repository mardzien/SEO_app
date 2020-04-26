import uuid
from services.senuto.audyt.main import generate_audit


def call_api(params):
    uid = uuid.uuid4()
    # print(f"Ten uid, to jest taki: {uid}")
    print('Calling API...')
    domain_name = params['domain_name']
    generate_audit(domain_name)
    return dict(status="Pending", params=params, uid=uid)
