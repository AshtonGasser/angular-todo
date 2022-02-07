import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { Task } from '../../Task';
@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css'],
})
export class TasksComponent implements OnInit {
  tasks: Task[] = [];
  constructor(private taskService: TaskService) {}

  //normally you want to use observables here if you're using async data
  //if you're fetching from a server

  ngOnInit(): void {
    //subscribe is kind of like a promise
    this.taskService.getTasks().subscribe((tasks) => (this.tasks = tasks));
  }

  deleteTask(task: Task) {
    this.taskService
      .deleteTask(task)
      .subscribe(
        () => (this.tasks = this.tasks.filter((t) => t.id! !== task.id))
      );
  }
  toggleReminder (task: Task) {
    task.reminder = !task.reminder;
    this.taskService.updateTaskReminder(task).subscribe()

  }
  addTask(task: Task) {
    
  }
}
