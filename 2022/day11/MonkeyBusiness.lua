-- http://lua-users.org/wiki/FileInputOutput

-- see if the file exists
function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

-- get all lines from a file, returns an empty 
-- list/table if the file does not exist
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

-- tests the functions above
local file = 'monkeysSample.txt'
local lines = lines_from(file)

-- print all line numbers and their contents
for k,v in pairs(lines) do
    local linesplit = {}
    for word in v:gmatch("%S+") do table.insert(linesplit, word) end

    if tablelen(linesplit) == 0 then
        print()
    end

    for k2, w in pairs(linesplit) do
        print(w)
    end
    print("-")
end