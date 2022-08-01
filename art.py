DEAL_PROMPT = "Deal the next cards (Y/N)?"

LOGO = """.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""               

OPTION_BOXES = '''\t -----------          ----------- 
\t|    HIT    |        |   STAND   |
\t|    (Y)    |        |    (N)    |
\t -----------          ----------- '''

BUST = ''' __^^^^^__                                       __^^^^^__ 
\\\\  \\     \\                                     /     /  //
 \\\\  \\    ---------------------------------------    /  // 
  \\\\  \\    ██████╗ ██╗   ██╗███████╗████████╗██╗    /  //  
   \\\\  \\   ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║   /  //   
    \\\\  \\  ██████╔╝██║   ██║███████╗   ██║   ██║  /  //    
    //  /  ██╔══██╗██║   ██║╚════██║   ██║   ╚═╝  \\  \\\\    
   //  /   ██████╔╝╚██████╔╝███████║   ██║   ██╗   \\  \\\\   
  //  /    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝    \\  \\\\  
 //  /    ---------------------------------------    \\  \\\\ 
//__<><>__/                                     \\__<><>__\\\\'''

WIN = '''      __^^^^^__                            __^^^^^__       
     \\\\  \\     \\                          /     /  //      
      \\\\  \\    ----------------------------    /  //       
       \\\\  \\    ██╗    ██╗██╗███╗   ██╗██╗    /  //        
        \\\\  \\   ██║    ██║██║████╗  ██║██║   /  //         
         \\\\  \\  ██║ █╗ ██║██║██╔██╗ ██║██║  /  //          
         //  /  ██║███╗██║██║██║╚██╗██║╚═╝  \\  \\\\          
        //  /   ╚███╔███╔╝██║██║ ╚████║██╗   \\  \\\\         
       //  /     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝    \\  \\\\        
      //  /    ----------------------------    \\  \\\\       
     //__<><>__/                          \\__<><>__\\\\      '''

PUSH = ''''''

BLACKJACK = ''' __^^^^^__                                                                             __^^^^^__ 
\\\\  \\     \\                                                                           /     /  //
 \\\\  \\    -----------------------------------------------------------------------------    /  // 
  \\\\  \\    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗██╗    /  //  
   \\\\  \\   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝██║   /  //   
    \\\\  \\  ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ ██║  /  //    
    //  /  ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ ╚═╝  \\  \\\\    
   //  /   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗██╗   \\  \\\\   
  //  /    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝    \\  \\\\  
 //  /    -----------------------------------------------------------------------------    \\  \\\\ 
//__<><>__/                                                                           \\__<><>__\\\\'''

end_conditions = {
    "BUST": BUST,
    "WIN": WIN,
    "PUSH": PUSH,
    "BLACKJACK": BLACKJACK
}