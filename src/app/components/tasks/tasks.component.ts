import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import {Task} from '../../Task'
@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {
tasks: Task[] = [];
  constructor(private taskService : TaskService) { }

  //normally you want to use observables here if you're using async data
  //if you're fetching from a server

  ngOnInit(): void {
    //subscribe is kind of like a promise
    this.taskService.getTasks().subscribe((tasks) => (this.tasks = tasks));
  }
}
