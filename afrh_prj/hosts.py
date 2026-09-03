import re

from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"afrh_prj"), "afrh_prj.urls", name="afrh_prj"),
)
