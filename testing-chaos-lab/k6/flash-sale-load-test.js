import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 100 },
    { duration: '1m', target: 1000 },
    { duration: '30s', target: 0 },
  ],
};

export default function () {
  const res = http.get('http://localhost:8081/api/v1/products/1');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(0.1);
}
