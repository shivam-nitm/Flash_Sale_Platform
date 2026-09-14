local key = KEYS[1]
local amount = tonumber(ARGV[1])
local current = tonumber(redis.call('get', key) or "0")
if current >= amount then
    redis.call('decrby', key, amount)
    return 1
else
    return 0
end
