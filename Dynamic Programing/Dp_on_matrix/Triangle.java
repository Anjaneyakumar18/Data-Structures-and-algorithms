class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<List<Integer>> dp = new ArrayList<>();
        dp.add(new ArrayList<>());
        dp.get(0).add(triangle.get(0).get(0));

        for (int i = 1; i < triangle.size(); i++) {
            dp.add(new ArrayList<>());
            for (int j = 0; j <= i; j++) {
                int val = triangle.get(i).get(j);
                if (j == 0) {
                    dp.get(i).add(val + dp.get(i - 1).get(0));
                } else if (j == i) {
                    dp.get(i).add(val + dp.get(i - 1).get(j - 1));
                } else {
                    int minAbove = Math.min(dp.get(i - 1).get(j - 1), dp.get(i - 1).get(j));
                    dp.get(i).add(val + minAbove);
                }
            }
        }

        return Collections.min(dp.get(triangle.size() - 1));
    }
}
