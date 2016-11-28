class Solution(object):
	def LengthOfLongestSubstring(self,s):

		string_lengths 	= [1 for letter in s]
		indices 		= {s[0] : [0]}
		current_range 	= [0,0]
		counter 		= 1


		while counter < len(s):
			
			if not s[counter] in indices.keys():
				indices[s[counter]] = [ counter ]
			else:
				indices[s[counter]].append( counter )
			matches 				= [ m for m in indices[s[counter]] if m >= current_range[0] and m <= current_range[1] ]
			

			if matches:
				string_lengths[current_range[0]] = current_range[1] - current_range[0] + 1
				current_range[1]				 = counter
				current_range[0]				 = matches[0] + 1
			else:
				current_range[1] 				+= 1

			counter 							+= 1


		return max(string_lengths)

solution = Solution()
print(solution.LengthOfLongestSubstring(10*'abcdefg'))