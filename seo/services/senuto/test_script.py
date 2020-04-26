from services.senuto.audyt.main import generate_audit


def call_api_sync(params):
    print('Calling API...')
    domain_name = params['domain_name']
    file_path = generate_audit(domain_name)
    return dict(status="OK", params=params, file_path=file_path)
