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

local file = 'monkeysSample.txt'
local lines = lines_from(file)
local monkeyArrStruct = {}
local currentInd = -1

for k,v in pairs(lines) do
    local linesplit = {}
    for word in v:gmatch("%S+") do table.insert(linesplit, word) end

    if tablelen(linesplit) == 0 then
        print()

    elseif linesplit[1] == "Monkey" then
        currentInd = linesplit[2]
        monkeyArrStruct[currentInd] = {}
        monkeyArrStruct[currentInd]["items"] = {}
        monkeyArrStruct[currentInd]["truefalse"] = {}

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
    
    elseif linesplit[1] == "If" then
        table.insert(monkeyArrStruct[currentInd]["truefalse"], linesplit[6])
    end

    for k2, w in pairs(linesplit) do
        print(w)
    end
    print("-")

end


print(monkeyArrStruct[currentInd]["tst"](monkeyArrStruct[currentInd]["op"](14)))

