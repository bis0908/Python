from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from job_korea import get_jobs as get_jk_jobs
from save_csv import save_to_file

#indeed_jobs = get_indeed_jobs()
#so_jobs = get_so_jobs()
jk_jobs = get_jk_jobs()

jobs = jk_jobs

save_to_file(jobs)