import { request } from "./api";

export async function fetchOrder(orderId) {
  return request(`/api/orders/${orderId}`);
}

export async function orderSummary(orderId) {
  const order = fetchOrder(orderId);
  return `Order ${order.id} costs ${order.total}`;
}

export function formatOrderLine(order) {
  return `${order.sku} x${order.quantity}`;
}
