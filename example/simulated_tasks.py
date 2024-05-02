# ONLY FOR JUPYTER ENVIRONMENT

import random
import time

from taskprogressbar import TaskProgressBar

def simulate_task_progress(progress_bar):
    task_ids = list(progress_bar.tasks.keys())
    total_tasks = len(task_ids)
    remaining_tasks = total_tasks
    
    try:
        while remaining_tasks > 0:
            task_id = random.choice(task_ids)
            current_status = progress_bar.tasks[task_id]
            
            if current_status == 'pending':
                new_status = 'ongoing'
            elif current_status == 'ongoing':
                new_status = random.choices(['success', 'failed', 'cached'], weights=(60, 30, 10), k=1)[0]
                if new_status != 'ongoing':
                    remaining_tasks -= 1
            else:
                continue
            
            progress_bar.update_task_status(task_id, new_status)
            time.sleep(random.uniform(0.1, 0.5))
    except KeyboardInterrupt:
        print("Simulation stopped by user.")

# Example usage
task_ids = [f"task_{i}" for i in range(2000)]
progress_bar = TaskProgressBar(task_ids)
progress_bar.display()

# Start the simulation of task updates
simulate_task_progress(progress_bar)