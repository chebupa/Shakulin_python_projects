# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-apece http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).


import re


def extract_domains_with_regex(file_path: str) -> list[str]:
    domains = []
    url_pattern = re.compile(r'https?://([^/\s:]+)')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = url_pattern.findall(line)
            domains.extend(matches)

    return domains


# Пример использования:
domains = extract_domains_with_regex("radio_stations.txt")
for domain in domains:
    print(domain)