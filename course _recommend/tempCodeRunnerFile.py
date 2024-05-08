 result_df=df.iloc[select_course_indices]
  result_df.loc[:,"similarity_score"]=select_course_score
  return result_df[["course_title","similarity_score","url","price","num_subscribers"]]