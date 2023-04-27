from typing import List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(content)


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    content = read(path)
    industries = [x['industry'] for x in content if x['industry'] != '']
    return set(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
