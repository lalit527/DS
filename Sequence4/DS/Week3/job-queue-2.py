# python3
from heapq import heappush, heappop

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
      queue = []
      n = self.num_workers
      self.start_times = []
      start_time = 0
      for i in range(len(self.jobs)):
        worker_thread = len(queue)
        execution_time = 0
        if len(queue) < n:
          execution_time = 0
          heappush(queue, (self.jobs[i], worker_thread))
        else:
          _ele = heappop(queue)
          start_time = _ele[0]
          execution_time = _ele[0]
          worker_thread = _ele[1]
          execution_time += self.jobs[i]
          heappush(queue, (execution_time, worker_thread))
        self.start_times.append((worker_thread, start_time))
      print(queue)
      print(self.start_times)


    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
          print('next_free_time', next_free_time)
        print('next_free_time2', next_free_time)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        # self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

