public class Solution1 {
//hashmap
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
        	if (map.containsKey(nums[i])){
        		if (i - map.get(nums[i]) <= k){
        			return true;
        		}
        		else{
        			map.put(nums[i], i);
        		}
        	}
        	else{
        		map.put(nums[i], i);
        	}

        }
        return false;
    }
}

public class Solution2 {
//set
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++){
        	if (i > k) set.remove(nums[i - k - 1]);
        	if (!set.add(nums[i])) return true;
        }
        return false;
    }
}
