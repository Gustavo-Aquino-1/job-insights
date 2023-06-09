from typing import Union, List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(content)


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    content = read(path)
    return max(
        [
            float(x["max_salary"])
            for x in content
            if x["max_salary"].isnumeric()
        ]
    )


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    content = read(path)
    return min(
        [
            float(x["min_salary"])
            for x in content
            if x["min_salary"].isnumeric()
        ]
    )


def validate(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
        not str(job["min_salary"]).isnumeric()
        or not str(job["max_salary"]).isnumeric()
    ):
        raise ValueError
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    validate(job, salary)
    try:
        if int(salary) >= int(job["min_salary"]) and int(salary) <= int(
            job["max_salary"]
        ):
            return True
        return False
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            res = matches_salary_range(job, salary)
        except Exception:
            pass
        else:
            if res:
                filtered_jobs.append(job)
    return filtered_jobs
