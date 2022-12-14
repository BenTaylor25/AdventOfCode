-- http://lua-users.org/wiki/FileInputOutput

function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

function lines_from(file)
  if not file_exists(file) then return {} end
  local lines = {}
  for line in io.lines(file) do 
    lines[#lines + 1] = line
  end
  return lines
end

function tablelen(t)
    local count = 0
    for _ in pairs(t) do count = count + 1 end
    return count
end

function intof(s)
    local nocomma = string.gsub(s, "%,", "")
    return tonumber(nocomma)
end

local file = 'monkeysActual.txt'
local lines = lines_from(file)
local monkeyArrStruct = {}
local allInds = {}
local currentInd = -1
local allDivisors = {}

for k,v in pairs(lines) do
    local linesplit = {}
    for word in v:gmatch("%S+") do table.insert(linesplit, word) end

    if tablelen(linesplit) == 0 then
        -- print()

    elseif linesplit[1] == "Monkey" then
        table.insert(allInds, linesplit[2])
        currentInd = linesplit[2]
        monkeyArrStruct[currentInd] = {}
        monkeyArrStruct[currentInd]["items"] = {}
        monkeyArrStruct[currentInd]["truefalse"] = {}
        monkeyArrStruct[currentInd]["inspected"] = 0

    elseif linesplit[1] == "Starting" then
        for i, v in pairs(linesplit) do
            if i > 2 then
                table.insert(monkeyArrStruct[currentInd]["items"], intof(v))
            end
        end

    elseif linesplit[1] == "Operation:" then
        monkeyArrStruct[currentInd]["op"] = load(string.format([[
            local old = ...
            return old %s %s
        ]], linesplit[5], linesplit[6]))

    elseif linesplit[1] == "Test:" then
        monkeyArrStruct[currentInd]["tst"] = load(string.format([[
            local op = ...
            return op %% %s == 0
        ]], linesplit[4]))
        table.insert(allDivisors, tonumber(linesplit[4]))
    
    elseif linesplit[1] == "If" then
        table.insert(monkeyArrStruct[currentInd]["truefalse"], linesplit[6])
    end

    -- for k2, w in pairs(linesplit) do
    --     print(w)
    -- end
    -- print("-")

end

-- print(monkeyArrStruct[currentInd]["tst"](monkeyArrStruct[currentInd]["op"](14)))

function findLCM(t)
    if tablelen(t) == 1 then
        return t[1]
    end

    local astart = table.remove(t, 1)
    local bstart = table.remove(t, 1)
    local a = astart
    local b = bstart

    while a ~= b do
        if a < b then
            a = a + astart
        else
            b = b + bstart
        end
    end

    table.insert(t, a)
    return findLCM(t)
end

LCM = findLCM(allDivisors)

function MonkeyAction(ind)
    local items = monkeyArrStruct[ind]["items"]
    while tablelen(items) > 0 do
        local item = table.remove(items, 1)

        -- inspect
        item = monkeyArrStruct[ind]["op"](item)
        monkeyArrStruct[ind]["inspected"] = monkeyArrStruct[ind]["inspected"] + 1

        -- handle int overflow
        item = item % LCM

        -- check divisible --
        local b = monkeyArrStruct[ind]["tst"](item)

        local passto = ""
        if b then
            passto = monkeyArrStruct[ind]["truefalse"][1] .. ":"
        else
            passto = monkeyArrStruct[ind]["truefalse"][2] .. ":"
        end

        -- pass to
        table.insert(monkeyArrStruct[passto]["items"], item)
    end
end

for round = 1, 10000 do
    for _, ind in pairs(allInds) do
        MonkeyAction(ind)
    end
end

-- print()

local inspected = {}
for _, ind in pairs(allInds) do
    print("num of items monkey has inspected: " .. monkeyArrStruct[ind]["inspected"])
    table.insert(inspected, monkeyArrStruct[ind]["inspected"])
    for _, v in pairs(monkeyArrStruct[ind]["items"]) do
        print("item worry: " .. v)
    end
    print()
end
print()

function popMax(t)
    local maxi = 1
    for i, v in pairs(t) do
        if v > t[maxi] then
            maxi = i
        end
    end
    return table.remove(t, maxi)
end

local m1 = popMax(inspected)
local m2 = popMax(inspected)

local monkeyBusiness = m1 * m2

print("monkey business: " .. monkeyBusiness)
