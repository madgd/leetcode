public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<Integer> intersect = new ArrayList<>();
        for (int i : nums1) {
            if (!map.containsKey(i)){
            	map.put(i, 1);
            }
            else{
            	map.put(i, map.get(i) + 1);
            }
        }
        for (int i : nums2) {
        	if (map.containsKey(i) && map.get(i)> 0){
        		intersect.add(i);
        		map.put(i, map.get(i) - 1);
        	}
        }

        int[] result = new int[intersect.size()];
        int i = 0;
        for (Integer num : intersect) {
            result[i++] = num;
        }
        return result;
    }
}
