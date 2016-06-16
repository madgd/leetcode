public class Solution1 {
    public static int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<Integer>();
        Set<Integer> set2 = new HashSet<>();
        Set<Integer> intersect = new HashSet<>();
        for (int i : nums1) {
            set1.add(i);
        }
        for (int i : nums2){
        	set2.add(i);
        }
        intersect.addAll(set1);
        intersect.retainAll(set2);
        int[] result = new int[intersect.size()];
        int i = 0;
        for (Integer num : intersect) {
            result[i++] = num;
        }
        return result;
	}
}

public class Solution2 {
    public static int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<Integer> intersect = new ArrayList<>();
        for (int i : nums1) {
            if (!map.containsKey(i)){
            	map.put(i, 0);
            }
        }
        for (int i : nums2) {
        	if (map.containsKey(i) && map.get(i)==0){
        		intersect.add(i);
        		map.put(i, 1);
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
