import base64

script = b"aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBvcwoKCgpvcy5zeXN0ZW0oImNscyIpCnByaW50KCkKcHJpbnQoIiIiICBfX18gIF8gICAgICAgICAgICAgICAgICAgX19fICAgICAgICAgICAgICAgIAogfCAuIFx8IHxfICBfX18gLl8gXyAgX19fIC8gX18+IF9fXyAgX19fIC5fIF8gCiB8ICBfL3wgLiB8LyAuIFx8ICcgfC8gLl8+XF9fIFwvIHwgJzxfPiB8fCAnIHwKIHxffCAgfF98X3xcX19fL3xffF98XF9fXy48X19fL1xffF8uPF9fX3x8X3xffAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiIiIikKcHJpbnQoIiAgICAgICAgICAgICBEaXNlw7FhZG8gcG9yIEVsdG90aXoiKQpwcmludCgiICAgICAgICAgICAgICBnaXRodWIuY29tL0VsdG90aXoiKQpwcmludCgpCnByaW50KCkKcHJpbnQoIiIiICAgTm90YTogTm8gYcOxYWRhIGVzcGFjaW9zIG5pIHNpbWJvbG9zIGNvbW8gIisiIG8veSAiLSIgIiIiKQpwcmludCgpCnByaW50KCkKbnVtYmVyID0gaW5wdXQoIiAgSW5zZXJ0ZSBudW1lcm8gZGUgdGVsZWZvbm8gPj4gIikgCnByaW50KCkgCmtleSA9ICJhYzM2N2FlY2MzYjk5YTUyNDkwNmE3NjE3ZGRkOGEzYiIKdXJsID0gImh0dHA6Ly9hcGlsYXllci5uZXQvYXBpL3ZhbGlkYXRlP2FjY2Vzc19rZXk9IiArIGtleSArICImbnVtYmVyPSIgKyBudW1iZXIKcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQodXJsKSAKYW5zd2VyID0gcmVzcG9uc2UuanNvbigpIAp0aW1lLnNsZWVwKDEpCnByaW50KCkgCmlmIGFuc3dlclsidmFsaWQiXSA9PSBUcnVlOgoJb3Muc3lzdGVtKCJjbHMiKQoJcHJpbnQoIiIiICBfX18gIF8gICAgICAgICAgICAgICAgICAgX19fICAgICAgICAgICAgICAgIAogfCAuIFx8IHxfICBfX18gLl8gXyAgX19fIC8gX18+IF9fXyAgX19fIC5fIF8gCiB8ICBfL3wgLiB8LyAuIFx8ICcgfC8gLl8+XF9fIFwvIHwgJzxfPiB8fCAnIHwKIHxffCAgfF98X3xcX19fL3xffF98XF9fXy48X19fL1xffF8uPF9fX3x8X3xffAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiIiIikKCXByaW50KCIgICAgICAgICAgICAgRGlzZcOxYWRvIHBvciBFbHRvdGl6IikKCXByaW50KCIgICAgICAgICAgICAgIGdpdGh1Yi5jb20vRWx0b3RpeiIpCglwcmludCgpCglwcmludCgpCglwcmludCgiICAgICBDaGVja2VhbmRvIE51bXZlcmlmeSBBUEkuLi4iKSAKCXByaW50KCJfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIpCglwcmludCgifCAgIFshXSBOdW1lcm8gVGVsZWZvbmljbzoiLGFuc3dlclsibnVtYmVyIl0pCglwcmludCgifCIpCglwcmludCgifCAgIFshXSBGb3JtYXRvIEludGVybmFjaW9uYWw6IixhbnN3ZXJbImludGVybmF0aW9uYWxfZm9ybWF0Il0pCglwcmludCgifCIpCglwcmludCgifCAgIFshXSBQcmVmaXggZGVsIFBhaXM6IixhbnN3ZXJbImNvdW50cnlfcHJlZml4Il0pCglwcmludCgifCIpIAoJcHJpbnQoInwgICBbIV0gTm9tYnJlIGRlbCBQYWlzOiIsYW5zd2VyWyJjb3VudHJ5X25hbWUiXSkKCXByaW50KCJ8IikKCXByaW50KCJ8ICAgWyFdIExvY2FsaXphY2lvbjoiLGFuc3dlclsibG9jYXRpb24iXSkKCXByaW50KCJ8IikKCXByaW50KCJ8ICAgWyFdIENhcnJpZXI6IixhbnN3ZXJbImNhcnJpZXIiXSkKCXByaW50KCJ8IikKCXByaW50KCJ8ICAgWyFdIFRpcG8gZGUgTGluZWE6IixhbnN3ZXJbImxpbmVfdHlwZSJdKQoJcHJpbnQoInxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIpCglwcmludCgpCglwcmludCgpCglwcmludCgiICAgICAgICBFc2NhbmVvIGZpbmFsaXphZG8uIikKZWxzZToKCW9zLnN5c3RlbSgiY2xzIikKCXByaW50KCIiIiAgX19fICBfICAgICAgICAgICAgICAgICAgIF9fXyAgICAgICAgICAgICAgICAKIHwgLiBcfCB8XyAgX19fIC5fIF8gIF9fXyAvIF9fPiBfX18gIF9fXyAuXyBfIAogfCAgXy98IC4gfC8gLiBcfCAnIHwvIC5fPlxfXyBcLyB8ICc8Xz4gfHwgJyB8CiB8X3wgIHxffF98XF9fXy98X3xffFxfX18uPF9fXy9cX3xfLjxfX198fF98X3wKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAoiIiIpCglwcmludCgiICAgICAgICAgICAgIERpc2XDsWFkbyBwb3IgRWx0b3RpeiIpCglwcmludCgiICAgICAgICAgICAgICBnaXRodWIuY29tL0VsdG90aXoiKQoJcHJpbnQoKQoJcHJpbnQoKQoJcHJpbnQoIiAgICAgQ2hlY2tlYW5kbyBOdW12ZXJpZnkgQVBJLi4uIikKCXByaW50KCkKCXByaW50KCkKCXByaW50KCIgICBOdW1lcm8gaW52YWxpZG8uIik="

exec(base64.b64decode(script))
