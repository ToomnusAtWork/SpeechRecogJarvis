# from keras.models import Model,load_model
# import numpy as np
# from utils import load_data
# import argparse


# file_path='data/cmn.txt'
# n_units = 256
# batch_size = 64
# epoch = 20
# num_samples = 10000


# input_texts,target_texts,input_dict,target_dict,target_dict_reverse,\
#     output_length,input_feature_length,output_feature_length,\
#     encoder_input,decoder_input,decoder_output=load_data(file_path,num_samples)


# def predict_chinese(source,encoder_inference, decoder_inference, n_steps, features):

#     state = encoder_inference.predict(source)

#     predict_seq = np.zeros((1,1,features))
#     predict_seq[0,0,target_dict['\t']] = 1

#     output = ''
#    
#     for i in range(n_steps):
#         
#         yhat,h,c = decoder_inference.predict([predict_seq]+state)
#         
#         char_index = np.argmax(yhat[0,-1,:])
#         char = target_dict_reverse[char_index]
#         output += char
#         state = [h,c]
#         predict_seq = np.zeros((1,1,features))
#         predict_seq[0,0,char_index] = 1
#         if char == '\n':
#             break
#     return output


# encoder_infer=load_model("result/encoder_infer.h5")
# decoder_infer=load_model("result/decoder_infer.h5")

# # for i in range(1000,1100):
# #     test = encoder_input[i:i+1,:,:]#i:i+1
# #     out = predict_chinese(test,encoder_infer,decoder_infer,output_length,output_feature_length)
# #     print(input_texts[i])
# #     print(out)


# if __name__ == '__main__':
#     parser=argparse.ArgumentParser(description="Please input an english sentence!")
#     parser.add_argument('--eng_sent','-e',required=True,help="an english sentence!")
#     args=parser.parse_args()

#     seq=args.eng_sent
#     input_length = max([len(i) for i in input_texts])
#     encoder_input = np.zeros((1, input_length, input_feature_length))
#     for char_index, char in enumerate(seq):
#         encoder_input[0, char_index, input_dict[char]] = 1
#     out = predict_chinese(encoder_input, encoder_infer, decoder_infer, output_length, output_feature_length)
#     print(out)