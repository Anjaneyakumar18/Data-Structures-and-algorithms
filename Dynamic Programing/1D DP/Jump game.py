class Solution {
    public boolean canJump(int[] nums) {
        
        int max_dist=0;
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(max_dist>=(n-1)){
                return true;
            }
            if(i>max_dist){
                return false;
            }
            max_dist=(max_dist>i+nums[i]?max_dist:i+nums[i]);
        }
        return true;
    }
}
