import { request, buildQuery } from "./api";

export function findUserById(users, userId) {
  return users.find((user) => user.id === userId);
}

export function sortUsersByName(users) {
  return [...users].sort((a, b) => a.displayName.localeCompare(b.displayName));
}

export async function fetchUser(userId) {
  return request(`/api/users/${userId}`);
}

export async function fetchUserOrders(userId, status) {
  const query = buildQuery({ status });
  return request(`/api/users/${userId}/orders?${query}`);
}

export async function loadUserSummary(userId) {
  // BUG (missing await): fetchUser returns a promise, so `user` is a Promise and
  // user.displayName is undefined rather than the name.
  const user = fetchUser(userId);
  return `${user.displayName} (${userId})`;
}
