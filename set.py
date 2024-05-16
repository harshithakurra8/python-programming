st={1,7,5,5}
print(st)

st={2,6,8,9}
st.discard(9)
print(st)

st={2,6,8,9}
st.remove(9)
print(st)

st={2,6,8,9}
st.add(5)
print(st)

coupons={"cpu","hdmi","psu","port"}
store={"cpu","hdmi","alu","psu","mouse","port"}
print(coupons.intersection(store))

coupons={"cpu","hdmi","psu","port"}
store={"cpu","hdmi","alu","psu","mouse","port"}
print(store.difference(coupons))

coupons={"cpu","hdmi","psu","port"}
store={"cpu","hdmi","alu","psu","mouse","port"}
print(store.symmetric_difference(coupons))

coupons={"cpu","hdmi","psu","port"}
store={"cpu","hdmi","alu","psu","mouse","port"}
print(store.union(coupons))


