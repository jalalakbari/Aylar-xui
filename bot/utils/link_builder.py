def build_config_link(subdomain, port, user_config):
    """
    ساخت لینک کانفیگ برای کاربر با توجه به ساب دامین و پورت مشخص شده
    """
    base_url = f"https://{subdomain}:{port}"
    config_link = f"{base_url}/configs/{user_config}"
    return config_link
