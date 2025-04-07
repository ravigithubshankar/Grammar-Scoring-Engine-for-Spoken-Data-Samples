from torch.utils.data import DataLoader
import torch.nn as nn
from transformers import BertModel
from Dataloader import dataset

BATCH_SIZE = 16

dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

class BERT_BiLSTM_Regression(nn.Module):
    def __init__(self, hidden_dim=128, num_layers=1, dropout=0.3):
        super(BERT_BiLSTM_Regression, self).__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.lstm = nn.LSTM(
            input_size=768,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            bidirectional=True
        )
        self.dropout = nn.Dropout(dropout)
        self.regressor = nn.Linear(hidden_dim * 2, 1)

    def forward(self, input_ids, attention_mask):
        with torch.no_grad():  # freeze BERT for now (can fine-tune later)
            bert_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        
        sequence_output = bert_output.last_hidden_state  # (batch, seq_len, 768)
        lstm_out, _ = self.lstm(sequence_output)         # (batch, seq_len, hidden*2)
        final_hidden = lstm_out[:, -1, :]                # last timestep
        x = self.dropout(final_hidden)
        output = self.regressor(x)
        return output.squeeze()
      
model = BERT_BiLSTM_Regression().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
loss_fn = nn.MSELoss()  # Or switch to Pearson/CCC Loss

model.train()
for epoch in range(50):  # You can increase this
    total_loss = 0
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1} | Loss: {total_loss:.4f}")
torch.save(model.state_dict(), "bert_bilstm_regression.pth")
print(" Model saved as bert_bilstm_regression.pth")
tokenizer.save_pretrained("bert_tokenizer/")
