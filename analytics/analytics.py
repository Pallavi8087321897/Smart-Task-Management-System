import pandas as pd
import numpy as np
from models.task import Task

def task_analytics():

    tasks = Task.query.all()

    data = []

    for t in tasks:

        data.append({
            "status": t.status
        })

    # IF NO TASKS
    if len(data) == 0:

        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        }

    df = pd.DataFrame(data)

    total_tasks = len(df)

    completed_tasks = len(
        df[df['status'] == 'Completed']
    )

    pending_tasks = len(
        df[df['status'] == 'Pending']
    )

    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": float(completion_percentage)
    }