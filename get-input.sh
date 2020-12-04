DAY=$(($(date -d "now" +%d)))
echo "Today is day $DAY"

. ./.env
mkdir "day$DAY"
cd day$DAY
curl --silent -o input.txt --cookie "session=$AOC_SESSION" https://adventofcode.com/2020/day/$DAY/input
cd -
